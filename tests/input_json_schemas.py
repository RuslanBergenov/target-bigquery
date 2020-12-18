schema_simple_1 = '{ "type": "SCHEMA", "stream": "simple_stream", "schema": { "properties": { "id": { "type": [ "null", "string" ] }, "name": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "integer" ] }, "ratio": { "type": [ "null", "number" ] }, "timestamp": { "type": "string", "format": "date-time" }, "date": { "type": "string", "format": "date" } }, "type": [ "null", "object" ] }, "key_properties": [ "id" ], "bookmark_properties": [ "date" ] }'



schema_simple_2_short = """{ "type": "SCHEMA", 
    "stream": "simple_stream", 
    "schema": { 
        "properties":   {  "timestamp": { "type": "string", "format": "date-time" },
                            "date": { "type": "string", "format": "date" } 
                        }, "type": [ "null", "object" ] }, "key_properties": [ "id" ], "bookmark_properties": [ "date" ] }
                        """


# schema_nested_1 - method 2 of schema conversion ("simplify and convert") fails

    # Simplifying function

        # input:
        # { "age": { "type": [ "null", "integer", "string" ] }

        # output of simplifying:
        # 'age': {'anyOf': [{'type': ['integer', 'null']}, {'type': ['string', 'null']}]}

        #anyOf appears this causes our conversion to fail


schema_nested_1 =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": { "account_id": { "type": [ "null", "string" ] }, "account_name": { "type": [ "null", "string" ] }, "action_values": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "ad_id": { "type": [ "null", "string" ] }, "ad_name": { "type": [ "null", "string" ] }, "adset_id": { "type": [ "null", "string" ] }, "adset_name": { "type": [ "null", "string" ] }, "age": { "type": [ "null", "integer", "string" ] }, "campaign_id": { "type": [ "null", "string" ] }, "campaign_name": { "type": [ "null", "string" ] }, "canvas_avg_view_percent": { "type": [ "null", "number" ] }, "canvas_avg_view_time": { "type": [ "null", "number" ] }, "clicks": { "type": [ "null", "integer" ] }, "conversion_rate_ranking": { "type": [ "null", "string" ] }, "cost_per_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_inline_link_click": { "type": [ "null", "number" ] }, "cost_per_inline_post_engagement": { "type": [ "null", "number" ] }, "cost_per_unique_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_unique_click": { "type": [ "null", "number" ] }, "cost_per_unique_inline_link_click": { "type": [ "null", "number" ] }, "cpc": { "type": [ "null", "number" ] }, "cpm": { "type": [ "null", "number" ] }, "cpp": { "type": [ "null", "number" ] }, "ctr": { "type": [ "null", "number" ] }, "date_start": { "format": "date-time", "type": [ "null", "string" ] }, "date_stop": { "format": "date-time", "type": [ "null", "string" ] }, "engagement_rate_ranking": { "type": [ "null", "string" ] }, "frequency": { "type": [ "null", "number" ] }, "gender": { "type": [ "null", "string" ] }, "impressions": { "type": [ "null", "integer" ] }, "inline_link_click_ctr": { "type": [ "null", "number" ] }, "inline_link_clicks": { "type": [ "null", "integer" ] }, "inline_post_engagement": { "type": [ "null", "integer" ] }, "objective": { "type": [ "null", "string" ] }, "outbound_clicks": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "quality_ranking": { "type": [ "null", "string" ] }, "reach": { "type": [ "null", "integer" ] }, "social_spend": { "type": [ "null", "number" ] }, "spend": { "type": [ "null", "number" ] }, "unique_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "unique_clicks": { "type": [ "null", "integer" ] }, "unique_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_click_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_clicks": { "type": [ "null", "integer" ] }, "unique_link_clicks_ctr": { "type": [ "null", "number" ] }, "video_30_sec_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p100_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p25_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p50_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p75_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'


schema_nested_1_subset_1_contains_age =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": { "age": { "type": [ "null", "integer", "string" ] }, "campaign_id": { "type": [ "null", "string" ] }, "campaign_name": { "type": [ "null", "string" ] }, "canvas_avg_view_percent": { "type": [ "null", "number" ] }, "canvas_avg_view_time": { "type": [ "null", "number" ] }, "clicks": { "type": [ "null", "integer" ] }, "conversion_rate_ranking": { "type": [ "null", "string" ] }, "cost_per_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_inline_link_click": { "type": [ "null", "number" ] }, "cost_per_inline_post_engagement": { "type": [ "null", "number" ] }, "cost_per_unique_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_unique_click": { "type": [ "null", "number" ] }, "cost_per_unique_inline_link_click": { "type": [ "null", "number" ] }, "cpc": { "type": [ "null", "number" ] }, "cpm": { "type": [ "null", "number" ] }, "cpp": { "type": [ "null", "number" ] }, "ctr": { "type": [ "null", "number" ] }, "date_start": { "format": "date-time", "type": [ "null", "string" ] }, "date_stop": { "format": "date-time", "type": [ "null", "string" ] }, "engagement_rate_ranking": { "type": [ "null", "string" ] }, "frequency": { "type": [ "null", "number" ] }, "gender": { "type": [ "null", "string" ] }, "impressions": { "type": [ "null", "integer" ] }, "inline_link_click_ctr": { "type": [ "null", "number" ] }, "inline_link_clicks": { "type": [ "null", "integer" ] }, "inline_post_engagement": { "type": [ "null", "integer" ] }, "objective": { "type": [ "null", "string" ] }, "outbound_clicks": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "quality_ranking": { "type": [ "null", "string" ] }, "reach": { "type": [ "null", "integer" ] }, "social_spend": { "type": [ "null", "number" ] }, "spend": { "type": [ "null", "number" ] }, "unique_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "unique_clicks": { "type": [ "null", "integer" ] }, "unique_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_click_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_clicks": { "type": [ "null", "integer" ] }, "unique_link_clicks_ctr": { "type": [ "null", "number" ] }, "video_30_sec_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p100_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p25_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p50_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p75_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'



# removed age
schema_nested_1_subset_2_no_age =  '{ "type": "SCHEMA", "stream": "nested_stream", "schema": { "properties": { "account_id": { "type": [ "null", "string" ] }, "account_name": { "type": [ "null", "string" ] }, "action_values": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "ad_id": { "type": [ "null", "string" ] }, "ad_name": { "type": [ "null", "string" ] }, "adset_id": { "type": [ "null", "string" ] }, "adset_name": { "type": [ "null", "string" ] }, "campaign_id": { "type": [ "null", "string" ] }, "campaign_name": { "type": [ "null", "string" ] }, "canvas_avg_view_percent": { "type": [ "null", "number" ] }, "canvas_avg_view_time": { "type": [ "null", "number" ] }, "clicks": { "type": [ "null", "integer" ] }, "conversion_rate_ranking": { "type": [ "null", "string" ] }, "cost_per_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_inline_link_click": { "type": [ "null", "number" ] }, "cost_per_inline_post_engagement": { "type": [ "null", "number" ] }, "cost_per_unique_action_type": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "string" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "cost_per_unique_click": { "type": [ "null", "number" ] }, "cost_per_unique_inline_link_click": { "type": [ "null", "number" ] }, "cpc": { "type": [ "null", "number" ] }, "cpm": { "type": [ "null", "number" ] }, "cpp": { "type": [ "null", "number" ] }, "ctr": { "type": [ "null", "number" ] }, "date_start": { "format": "date-time", "type": [ "null", "string" ] }, "date_stop": { "format": "date-time", "type": [ "null", "string" ] }, "engagement_rate_ranking": { "type": [ "null", "string" ] }, "frequency": { "type": [ "null", "number" ] }, "gender": { "type": [ "null", "string" ] }, "impressions": { "type": [ "null", "integer" ] }, "inline_link_click_ctr": { "type": [ "null", "number" ] }, "inline_link_clicks": { "type": [ "null", "integer" ] }, "inline_post_engagement": { "type": [ "null", "integer" ] }, "objective": { "type": [ "null", "string" ] }, "outbound_clicks": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "quality_ranking": { "type": [ "null", "string" ] }, "reach": { "type": [ "null", "integer" ] }, "social_spend": { "type": [ "null", "number" ] }, "spend": { "type": [ "null", "number" ] }, "unique_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "unique_clicks": { "type": [ "null", "integer" ] }, "unique_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_click_ctr": { "type": [ "null", "number" ] }, "unique_inline_link_clicks": { "type": [ "null", "integer" ] }, "unique_link_clicks_ctr": { "type": [ "null", "number" ] }, "video_30_sec_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p100_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p25_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p50_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_p75_watched_actions": { "items": { "properties": { "1d_click": { "type": [ "null", "number" ] }, "1d_view": { "type": [ "null", "number" ] }, "28d_click": { "type": [ "null", "number" ] }, "28d_view": { "type": [ "null", "number" ] }, "7d_click": { "type": [ "null", "number" ] }, "7d_view": { "type": [ "null", "number" ] }, "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "video_play_curve_actions": { "items": { "properties": { "action_type": { "type": [ "null", "string" ] }, "value": { "items": { "type": [ "null", "integer" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] }, "website_ctr": { "items": { "properties": { "action_destination": { "type": [ "null", "string" ] }, "action_target_id": { "type": [ "null", "string" ] }, "action_type": { "type": [ "null", "string" ] }, "value": { "type": [ "null", "number" ] } }, "type": [ "null", "object" ] }, "type": [ "null", "array" ] } }, "type": [ "null", "object" ] }, "key_properties": [ "campaign_id", "adset_id", "ad_id", "date_start", "age", "gender" ], "bookmark_properties": [ "date_start" ] }'




schema_nested_2 = '{"type": "SCHEMA", "stream": "campaigns", "schema": {"type": ["null", "object"], "additionalProperties": false, "properties": {"AudienceAdsBidAdjustment": {"type": ["null", "integer"]}, "BiddingScheme": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "InheritedBidStrategyType": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetCpa": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetRoas": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "MaxCpc": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Amount": {"type": ["null", "number"]}}}, "TargetAdPosition": {"type": ["null", "string"]}, "TargetImpressionShare": {"type": ["null", "number"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}, "BudgetType": {"type": ["null", "string"]}, "DailyBudget": {"type": ["null", "number"]}, "ExperimentId": {"type": ["null", "integer"]}, "FinalUrlSuffix": {"type": ["null", "string"]}, "ForwardCompatibilityMap": {"type": ["null", "object"], "properties": {"KeyValuePairOfstringstring": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"key": {"type": ["null", "string"]}, "value": {"type": ["null", "string"]}}}}}}, "Id": {"type": ["null", "integer"]}, "Name": {"type": ["null", "string"]}, "Status": {"type": ["null", "string"]}, "SubType": {"type": ["null", "string"]}, "TimeZone": {"type": ["null", "string"]}, "TrackingUrlTemplate": {"type": ["null", "string"]}, "UrlCustomParameters": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Parameters": {"type": ["null", "object"], "properties": {"CustomParameter": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"Key": {"type": ["null", "string"]}, "Value": {"type": ["null", "string"]}}}}}}}}, "CampaignType": {"type": ["null", "string"]}, "Settings": {"type": ["null", "object"], "properties": {"Setting": {"type": ["null", "array"], "items": {"anyOf": [{"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "Details": {"type": ["null", "object"], "properties": {"TargetSettingDetail": {"type": ["null", "array"], "items": {"type": ["null", "object"], "additionalProperties": false, "properties": {"CriterionTypeGroup": {"type": ["null", "string"]}, "TargetAndBid": {"type": ["boolean"]}}}}}}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "LocalInventoryAdsEnabled": {"type": ["null", "boolean"]}, "Priority": {"type": ["null", "integer"]}, "SalesCountryCode": {"type": ["null", "string"]}, "StoreId": {"type": ["null", "integer"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "BidBoostValue": {"type": ["null", "number"]}, "BidMaxValue": {"type": ["null", "number"]}, "BidOption": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}, "DomainName": {"type": ["null", "string"]}, "Language": {"type": ["null", "string"]}, "PageFeedIds": {"type": ["null", "object"], "properties": {"long": {"type": ["null", "array"], "items": {"type": "integer"}}}}, "Source": {"type": ["null", "string"]}}}, {"type": ["null", "object"], "additionalProperties": false, "properties": {"Type": {"type": ["null", "string"]}}}]}}}}, "BudgetId": {"type": ["null", "integer"]}, "Languages": {"type": ["null", "object"], "properties": {"string": {"type": ["null", "array"], "items": {"type": "string"}}}}, "AdScheduleUseSearcherTimeZone": {"type": ["null", "boolean"]}}}, "key_properties": ["Id"]}'


schema_nested_3_shopify = '{    "type":"SCHEMA",    "stream":"orders",    "schema": {        "properties": {          "address_id": {            "type": [              "null",              "string"            ]          },          "address_is_active": {            "type": [              "null",              "boolean"            ]          },          "billing_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "charge_id": {            "type": [              "null",              "string"            ]          },          "charge_status": {            "type": [              "null",              "string"            ]          },          "created_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "customer_id": {            "type": [              "null",              "string"            ]          },          "discount_codes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "amount": {                      "type": [                        "null",                        "number"                      ]                    },                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "type": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "email": {            "type": [              "null",              "string"            ]          },          "first_name": {            "type": [              "null",              "string"            ]          },          "hash": {            "type": [              "null",              "string"            ]          },          "id": {            "type": [              "null",              "string"            ]          },          "is_prepaid": {            "type": [              "null",              "boolean"            ]          },          "last_name": {            "type": [              "null",              "string"            ]          },          "line_items": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "grams": {                      "type": [                        "null",                        "integer"                      ]                    },                    "images": {                      "type": [                        "null",                        "object"                      ],                      "additionalProperties": false,                      "properties": {                        "large": {                          "type": [                            "null",                            "string"                          ]                        },                        "medium": {                          "type": [                            "null",                            "string"                          ]                        },                        "original": {                          "type": [                            "null",                            "string"                          ]                        },                        "small": {                          "type": [                            "null",                            "string"                          ]                        }                      }                    },                    "price": {                      "type": [                        "null",                        "number"                      ],                      "multipleOf": 1e-08                    },                    "properties": {                      "anyOf": [                        {                          "type": "array",                          "items": {                            "type": "object",                            "additionalProperties": false,                            "properties": {                              "name": {                                "type": [                                  "null",                                  "string"                                ]                              },                              "value": {                                "type": [                                  "null",                                  "string"                                ]                              }                            }                          }                        },                        {                          "type": "null"                        }                      ]                    },                    "quantity": {                      "type": [                        "null",                        "integer"                      ]                    },                    "shopify_product_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "shopify_variant_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "sku": {                      "type": [                        "null",                        "string"                      ]                    },                    "subscription_id": {                      "type": [                        "null",                        "string"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    },                    "variant_title": {                      "type": [                        "null",                        "string"                      ]                    },                    "vendor": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "note": {            "type": [              "null",              "string"            ]          },          "note_attributes": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "name": {                      "type": [                        "null",                        "string"                      ]                    },                    "value": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "payment_processor": {            "type": [              "null",              "string"            ]          },          "processed_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "scheduled_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipped_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_address": {            "properties": {              "address1": {                "type": [                  "null",                  "string"                ]              },              "address2": {                "type": [                  "null",                  "string"                ]              },              "city": {                "type": [                  "null",                  "string"                ]              },              "company": {                "type": [                  "null",                  "string"                ]              },              "country": {                "type": [                  "null",                  "string"                ]              },              "first_name": {                "type": [                  "null",                  "string"                ]              },              "last_name": {                "type": [                  "null",                  "string"                ]              },              "phone": {                "type": [                  "null",                  "string"                ]              },              "province": {                "type": [                  "null",                  "string"                ]              },              "zip": {                "type": [                  "null",                  "string"                ]              }            },            "type": [              "null",              "object"            ],            "additionalProperties": false          },          "shipping_date": {            "format": "date-time",            "type": [              "null",              "string"            ]          },          "shipping_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "shopify_cart_token": {            "type": [              "null",              "string"            ]          },          "shopify_customer_id": {            "type": [              "null",              "string"            ]          },          "shopify_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_id": {            "type": [              "null",              "string"            ]          },          "shopify_order_number": {            "type": [              "null",              "string"            ]          },          "status": {            "type": [              "null",              "string"            ]          },          "subtotal_price": {            "type": [              "null",              "number"            ]          },          "tags": {            "type": [              "null",              "string"            ]          },          "tax_lines": {            "anyOf": [              {                "type": "array",                "items": {                  "type": "object",                  "additionalProperties": false,                  "properties": {                    "code": {                      "type": [                        "null",                        "string"                      ]                    },                    "price": {                      "type": [                        "null",                        "number"                      ]                    },                    "title": {                      "type": [                        "null",                        "string"                      ]                    }                  }                }              },              {                "type": "null"              }            ]          },          "total_discounts": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_line_items_price": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_price": {            "type": [              "null",              "number"            ]          },          "total_refunds": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_tax": {            "multipleOf": 1e-08,            "type": [              "null",              "number"            ]          },          "total_weight": {            "type": [              "null",              "integer"            ]          },          "transaction_id": {            "type": [              "null",              "string"            ]          },          "type": {            "type": [              "null",              "string"            ]          },          "updated_at": {            "format": "date-time",            "type": [              "null",              "string"            ]          }        },        "type": "object",        "additionalProperties": false      },    "key_properties":[       "Id"    ] }'




# Bing Ads accounts

# This table has KeyValueOfstringbase column. It previously created an issue, while using method 1 of schema conversion.

#TODO: maybe remove these comments or hide name and link
# this is the version from Ben
bing_ads_accounts = '{"type":"SCHEMA","stream":"accounts","schema":{"type":["null","object"],"additionalProperties":false,"properties":{"BillToCustomerId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AccountFinancialStatus":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Language":{"type":["null","string"]},"LastModifiedByUserId":{"type":["null","integer"]},"LastModifiedTime":{"type":["null","string"],"format":"date-time"},"Name":{"type":["null","string"]},"Number":{"type":["null","string"]},"ParentCustomerId":{"type":["integer"]},"PaymentMethodId":{"type":["null","integer"]},"PaymentMethodType":{"type":["null","string"]},"PrimaryUserId":{"type":["null","integer"]},"AccountLifeCycleStatus":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"TimeZone":{"type":["null","string"]},"PauseReason":{"type":["null","integer"]},"ForwardCompatibilityMap":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"LinkedAgencies":{"type":["null","object"],"properties":{"CustomerInfo":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"Id":{"type":["null","integer"]},"Name":{"type":["null","string"]}}}}}},"SalesHouseCustomerId":{"type":["null","integer"]},"TaxInformation":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"BackUpPaymentInstrumentId":{"type":["null","integer"]},"BillingThresholdAmount":{"type":["null","number"]},"BusinessAddress":{"type":["null","object"],"additionalProperties":false,"properties":{"City":{"type":["null","string"]},"CountryCode":{"type":["null","string"]},"Id":{"type":["null","integer"]},"Line1":{"type":["null","string"]},"Line2":{"type":["null","string"]},"Line3":{"type":["null","string"]},"Line4":{"type":["null","string"]},"PostalCode":{"type":["null","string"]},"StateOrProvince":{"type":["null","string"]},"TimeStamp":{"type":["null","string"]},"BusinessName":{"type":["null","string"]}}},"AutoTagType":{"type":["null","string"]},"SoldToPaymentInstrumentId":{"type":["null","integer"]},"TaxCertificate":{"type":["null","object"],"additionalProperties":false,"properties":{"TaxCertificateBlobContainerName":{"type":["null","string"]},"TaxCertificates":{"type":["null","object"],"properties":{"KeyValueOfstringbase":{"type":["null","array"],"items":"KeyValueOfstringbase"}}},"Status":{"type":["null","string"]}}}}},"key_properties":[]}'


# this is the version from:
# https://bitbucket.org/analyticspros/dt-singerio-bingads/src/master/dt-tap-catalog.json 

bing_ads_accounts_v2 = """{
      "tap_stream_id": "accounts",
      "stream": "accounts",
      "schema": { "selected":true,
        "type": [
          "null",
          "object"
        ],
        "additionalProperties": false,
        "properties": {
          "BillToCustomerId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "CurrencyCode": {
            "type": [
              "null",
              "string"
            ]
          },
          "AccountFinancialStatus": {
            "type": [
              "null",
              "string"
            ]
          },
          "Id": {
            "type": [
              "null",
              "integer"
            ]
          },
          "Language": {
            "type": [
              "null",
              "string"
            ]
          },
          "LastModifiedByUserId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "LastModifiedTime": {
            "type": [
              "null",
              "string"
            ],
            "format": "date-time"
          },
          "Name": {
            "type": [
              "null",
              "string"
            ]
          },
          "Number": {
            "type": [
              "null",
              "string"
            ]
          },
          "ParentCustomerId": {
            "type": [
              "integer"
            ]
          },
          "PaymentMethodId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "PaymentMethodType": {
            "type": [
              "null",
              "string"
            ]
          },
          "PrimaryUserId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "AccountLifeCycleStatus": {
            "type": [
              "null",
              "string"
            ]
          },
          "TimeStamp": {
            "type": [
              "null",
              "string"
            ]
          },
          "TimeZone": {
            "type": [
              "null",
              "string"
            ]
          },
          "PauseReason": {
            "type": [
              "null",
              "integer"
            ]
          },
          "ForwardCompatibilityMap": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "KeyValuePairOfstringstring": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "key": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "value": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "LinkedAgencies": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "CustomerInfo": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "Id": {
                      "type": [
                        "null",
                        "integer"
                      ]
                    },
                    "Name": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "SalesHouseCustomerId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "TaxInformation": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "KeyValuePairOfstringstring": {
                "type": [
                  "null",
                  "array"
                ],
                "items": {
                  "type": [
                    "null",
                    "object"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "key": {
                      "type": [
                        "null",
                        "string"
                      ]
                    },
                    "value": {
                      "type": [
                        "null",
                        "string"
                      ]
                    }
                  }
                }
              }
            }
          },
          "BackUpPaymentInstrumentId": {
            "type": [
              "null",
              "integer"
            ]
          },
          "BillingThresholdAmount": {
            "type": [
              "null",
              "number"
            ]
          },
          "BusinessAddress": {
            "type": [
              "null",
              "object"
            ],
            "additionalProperties": false,
            "properties": {
              "City": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "CountryCode": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Id": {
                "type": [
                  "null",
                  "integer"
                ]
              },
              "Line1": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line2": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line3": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "Line4": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "PostalCode": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "StateOrProvince": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "TimeStamp": {
                "type": [
                  "null",
                  "string"
                ]
              },
              "BusinessName": {
                "type": [
                  "null",
                  "string"
                ]
              }
            }
          },
          "AutoTagType": {
            "type": [
              "null",
              "string"
            ]
          },
          "SoldToPaymentInstrumentId": {
            "type": [
              "null",
              "integer"
            ]
          }
        }
      },
      "key_properties": [
        "Id",
        "LastModifiedTime"
      ],
      "replication_key": "LastModifiedTime",
      "replication_method": "INCREMENTAL",
      "metadata": [
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PaymentMethodId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PrimaryUserId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "CurrencyCode"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Number"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "LinkedAgencies"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "ForwardCompatibilityMap"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AutoTagType"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "LastModifiedByUserId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "SoldToPaymentInstrumentId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Name"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PaymentMethodType"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TimeStamp"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "ParentCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TaxInformation"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BillingThresholdAmount"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BusinessAddress"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "TimeZone"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BackUpPaymentInstrumentId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "PauseReason"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "BillToCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AccountLifeCycleStatus"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "SalesHouseCustomerId"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "AccountFinancialStatus"
          ]
        },
        {
          "metadata": {
            "inclusion": "available"
          },
          "breadcrumb": [
            "properties",
            "Language"
          ]
        }
      ]
    }"""

# Bing Ads campaigns

bing_ads_campaigns = '{"type":"SCHEMA","stream":"campaigns","schema":{"type":["null","object"],"additionalProperties":false,"properties":{"AudienceAdsBidAdjustment":{"type":["null","integer"]},"BiddingScheme":{"anyOf":[{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetRoas":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"InheritedBidStrategyType":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetAdPosition":{"type":["null","string"]},"TargetImpressionShare":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"TargetRoas":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"MaxCpc":{"type":["null","object"],"additionalProperties":false,"properties":{"Amount":{"type":["null","number"]}}},"TargetCpa":{"type":["null","number"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}}]},"BudgetType":{"type":["null","string"]},"DailyBudget":{"type":["null","number"]},"ExperimentId":{"type":["null","integer"]},"FinalUrlSuffix":{"type":["null","string"]},"ForwardCompatibilityMap":{"type":["null","object"],"properties":{"KeyValuePairOfstringstring":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"key":{"type":["null","string"]},"value":{"type":["null","string"]}}}}}},"Id":{"type":["null","integer"]},"Name":{"type":["null","string"]},"Status":{"type":["null","string"]},"SubType":{"type":["null","string"]},"TimeZone":{"type":["null","string"]},"TrackingUrlTemplate":{"type":["null","string"]},"UrlCustomParameters":{"type":["null","object"],"additionalProperties":false,"properties":{"Parameters":{"type":["null","object"],"properties":{"CustomParameter":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"Key":{"type":["null","string"]},"Value":{"type":["null","string"]}}}}}}}},"CampaignType":{"type":["null","string"]},"Settings":{"type":["null","object"],"properties":{"Setting":{"type":["null","array"],"items":{"anyOf":[{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"DomainName":{"type":["null","string"]},"Language":{"type":["null","string"]},"PageFeedIds":{"type":["null","object"],"properties":{"long":{"type":["null","array"],"items":{"type":"integer"}}}},"Source":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"Details":{"type":["null","object"],"properties":{"TargetSettingDetail":{"type":["null","array"],"items":{"type":["null","object"],"additionalProperties":false,"properties":{"CriterionTypeGroup":{"type":["null","string"]},"TargetAndBid":{"type":["boolean"]}}}}}}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"LocalInventoryAdsEnabled":{"type":["null","boolean"]},"Priority":{"type":["null","integer"]},"SalesCountryCode":{"type":["null","string"]},"StoreId":{"type":["null","integer"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]},"BidBoostValue":{"type":["null","number"]},"BidMaxValue":{"type":["null","number"]},"BidOption":{"type":["null","string"]}}},{"type":["null","object"],"additionalProperties":false,"properties":{"Type":{"type":["null","string"]}}}]}}}},"BudgetId":{"type":["null","integer"]},"Languages":{"type":["null","object"],"properties":{"string":{"type":["null","array"],"items":{"type":"string"}}}},"AdScheduleUseSearcherTimeZone":{"type":["null","boolean"]}}},"key_properties":[]}'


# Bing Ads ad_extension_detail_report

bing_ads_ad_extension_detail_report = '{"type":"SCHEMA","stream":"ad_extension_detail_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdTitle":{"type":["null","string"]},"AdId":{"type":["null","integer"]},"AdExtensionType":{"type":["null","string"]},"AdExtensionTypeId":{"type":["null","string"]},"AdExtensionId":{"type":["null","string"]},"AdExtensionVersion":{"type":["null","string"]},"AdExtensionPropertyValue":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'


# Bing Ads ad_group_performance_report

bing_ads_ad_group_performance_report = '{"type":"SCHEMA","stream":"ad_group_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"Status":{"type":["null","string"]},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"DeviceType":{"type":["null","string"]},"Language":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"ImpressionSharePercent":{"type":["null","number"]},"ImpressionLostToBudgetPercent":{"type":["null","number"]},"ImpressionLostToRankAggPercent":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"PhoneImpressions":{"type":["null","integer"]},"PhoneCalls":{"type":["null","integer"]},"Ptr":{"type":["null","number"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupLabels":{"type":["null","string"]},"ExactMatchImpressionSharePercent":{"type":["null","number"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"ClickSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionSharePercent":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"TopImpressionShareLostToRankPercent":{"type":["null","string"]},"TopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToRankPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"TopImpressionSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AudienceImpressionSharePercent":{"type":["null","string"]},"AudienceImpressionLostToRankPercent":{"type":["null","string"]},"AudienceImpressionLostToBudgetPercent":{"type":["null","string"]},"RelativeCtr":{"type":["null","string"]},"AdGroupType":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads ad_performance_report

bing_ads_ad_performance_report = '{"type":"SCHEMA","stream":"ad_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdId":{"type":["null","integer"]},"AdGroupId":{"type":["null","integer"]},"AdTitle":{"type":["null","string"]},"AdDescription":{"type":["null","string"]},"AdDescription2":{"type":["null","string"]},"AdType":{"type":["null","string"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"DestinationUrl":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"Language":{"type":["null","string"]},"DisplayUrl":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"FinalUrl":{"type":["null","string"]},"FinalMobileUrl":{"type":["null","string"]},"FinalAppUrl":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"TitlePart1":{"type":["null","string"]},"TitlePart2":{"type":["null","string"]},"TitlePart3":{"type":["null","string"]},"Headline":{"type":["null","string"]},"LongHeadline":{"type":["null","string"]},"BusinessName":{"type":["null","string"]},"Path1":{"type":["null","string"]},"Path2":{"type":["null","string"]},"AdLabels":{"type":["null","string"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads age_gender_audience_report

bing_ads_age_gender_audience_report = '{"type":"SCHEMA","stream":"age_gender_audience_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdDistribution":{"type":["null","string"]},"AgeGroup":{"type":["null","string"]},"Gender":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"Spend":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ExtendedCost":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Language":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads audience_performance_report

bing_ads_audience_performance_report = '{"type":"SCHEMA","stream":"audience_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AudienceId":{"type":["null","string"]},"AudienceName":{"type":["null","string"]},"AssociationStatus":{"type":["null","string"]},"BidAdjustment":{"type":["null","string"]},"TargetingSetting":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"AudienceType":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"AssociationId":{"type":["null","string"]},"AssociationLevel":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads campaign_performance_report

bing_ads_campaign_performance_report = '{"type":"SCHEMA","stream":"campaign_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignStatus":{"type":["null","string"]},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"LowQualityClicks":{"type":["null","integer"]},"LowQualityClicksPercent":{"type":["null","number"]},"LowQualityImpressions":{"type":["null","integer"]},"LowQualityImpressionsPercent":{"type":["null","number"]},"LowQualityConversions":{"type":["null","integer"]},"LowQualityConversionRate":{"type":["null","number"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"ImpressionSharePercent":{"type":["null","number"]},"ImpressionLostToBudgetPercent":{"type":["null","number"]},"ImpressionLostToRankAggPercent":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"PhoneImpressions":{"type":["null","integer"]},"PhoneCalls":{"type":["null","integer"]},"Ptr":{"type":["null","number"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"BudgetName":{"type":["null","string"]},"BudgetStatus":{"type":["null","string"]},"BudgetAssociationStatus":{"type":["null","string"]},"LowQualityGeneralClicks":{"type":["null","integer"]},"LowQualitySophisticatedClicks":{"type":["null","integer"]},"CampaignLabels":{"type":["null","string"]},"ExactMatchImpressionSharePercent":{"type":["null","number"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"ClickSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionSharePercent":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"TopImpressionShareLostToRankPercent":{"type":["null","string"]},"TopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToRankPercent":{"type":["null","string"]},"AbsoluteTopImpressionShareLostToBudgetPercent":{"type":["null","string"]},"TopImpressionSharePercent":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AudienceImpressionSharePercent":{"type":["null","string"]},"AudienceImpressionLostToRankPercent":{"type":["null","string"]},"AudienceImpressionLostToBudgetPercent":{"type":["null","string"]},"RelativeCtr":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads geographic_performance_report

bing_ads_geographic_performance_report = '{"type":"SCHEMA","stream":"geographic_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Country":{"type":["null","string"]},"State":{"type":["null","string"]},"MetroArea":{"type":["null","string"]},"City":{"type":["null","string"]},"CurrencyCode":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"ProximityTargetLocation":{"type":["null","string"]},"Radius":{"type":["null","number"]},"Language":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"LocationType":{"type":["null","string"]},"MostSpecificLocation":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"County":{"type":["null","string"]},"PostalCode":{"type":["null","string"]},"LocationId":{"type":["null","integer"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads goals_and_funnels_report

bing_ads_goals_and_funnels_report = '{"type":"SCHEMA","stream":"goals_and_funnels_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Keyword":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"Goal":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"AllRevenue":{"type":["null","string"]},"GoalId":{"type":["null","integer"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads keyword_performance_report

bing_ads_keyword_performance_report = '{"type":"SCHEMA","stream":"keyword_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"Keyword":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"AdId":{"type":["null","integer"]},"AdType":{"type":["null","string"]},"DestinationUrl":{"type":["null","string"]},"CurrentMaxCpc":{"type":["null","number"]},"CurrencyCode":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"AdDistribution":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"BidMatchType":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"QualityScore":{"type":["null","number"]},"ExpectedCtr":{"type":["null","number"]},"AdRelevance":{"type":["null","number"]},"LandingPageExperience":{"type":["null","number"]},"Language":{"type":["null","string"]},"HistoricalQualityScore":{"type":["null","string"]},"HistoricalExpectedCtr":{"type":["null","string"]},"HistoricalAdRelevance":{"type":["null","string"]},"HistoricalLandingPageExperience":{"type":["null","string"]},"QualityImpact":{"type":["null","number"]},"CampaignStatus":{"type":["null","string"]},"AccountStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"TrackingTemplate":{"type":["null","string"]},"CustomParameters":{"type":["null","string"]},"FinalUrl":{"type":["null","string"]},"FinalMobileUrl":{"type":["null","string"]},"FinalAppUrl":{"type":["null","string"]},"BidStrategyType":{"type":["null","string"]},"KeywordLabels":{"type":["null","string"]},"Mainline1Bid":{"type":["null","number"]},"MainlineBid":{"type":["null","number"]},"FirstPageBid":{"type":["null","string"]},"FinalUrlSuffix":{"type":["null","string"]},"BaseCampaignId":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"ViewThroughConversions":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'

# Bing Ads search_query_performance_report

bing_ads_search_query_performance_report = '{"type":"SCHEMA","stream":"search_query_performance_report","schema":{"properties":{"AccountName":{"type":["null","string"]},"AccountNumber":{"type":["null","string"]},"AccountId":{"type":["null","integer"]},"TimePeriod":{"type":["null","string"],"format":"date-time"},"CampaignName":{"type":["null","string"]},"CampaignId":{"type":["null","integer"]},"AdGroupName":{"type":["null","string"]},"AdGroupId":{"type":["null","integer"]},"AdId":{"type":["null","integer"]},"AdType":{"type":["null","string"]},"DestinationUrl":{"type":["null","string"]},"BidMatchType":{"type":["null","string"]},"DeliveredMatchType":{"type":["null","string"]},"CampaignStatus":{"type":["null","string"]},"AdStatus":{"type":["null","string"]},"Impressions":{"type":["null","integer"]},"Clicks":{"type":["null","integer"]},"Ctr":{"type":["null","number"]},"AverageCpc":{"type":["null","number"]},"Spend":{"type":["null","number"]},"AveragePosition":{"type":["null","number"]},"SearchQuery":{"type":["null","string"]},"Keyword":{"type":["null","string"]},"AdGroupCriterionId":{"type":["null","integer"]},"Conversions":{"type":["null","number"]},"ConversionRate":{"type":["null","number"]},"CostPerConversion":{"type":["null","number"]},"Language":{"type":["null","string"]},"KeywordId":{"type":["null","integer"]},"Network":{"type":["null","string"]},"TopVsOther":{"type":["null","string"]},"DeviceType":{"type":["null","string"]},"DeviceOS":{"type":["null","string"]},"Assists":{"type":["null","integer"]},"Revenue":{"type":["null","number"]},"ReturnOnAdSpend":{"type":["null","number"]},"CostPerAssist":{"type":["null","number"]},"RevenuePerConversion":{"type":["null","number"]},"RevenuePerAssist":{"type":["null","number"]},"AccountStatus":{"type":["null","string"]},"AdGroupStatus":{"type":["null","string"]},"KeywordStatus":{"type":["null","string"]},"CampaignType":{"type":["null","string"]},"CustomerId":{"type":["null","string"]},"CustomerName":{"type":["null","string"]},"AllConversions":{"type":["null","string"]},"AllRevenue":{"type":["null","string"]},"AllConversionRate":{"type":["null","string"]},"AllCostPerConversion":{"type":["null","string"]},"AllReturnOnAdSpend":{"type":["null","string"]},"AllRevenuePerConversion":{"type":["null","string"]},"Goal":{"type":["null","string"]},"GoalType":{"type":["null","string"]},"AbsoluteTopImpressionRatePercent":{"type":["null","string"]},"TopImpressionRatePercent":{"type":["null","string"]},"_sdc_report_datetime":{"type":"string","format":"date-time"}},"additionalProperties":false,"type":"object"},"key_properties":[]}'