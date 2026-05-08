# IAnnotation Interface Methods

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_methods`

Allows access to notes, weld symbols, datum tags, display dimensions, blocks, cosmetic threads, center marks, centerlines, and other annotation types.
For a list of all members of this type, see [IAnnotation members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddOrUpdateStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.md) | Adds or updates the annotation linked to the specified style. |
| Method | [ApplyDefaultStyleAttributes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.md) | Applies the default style attribute to this annotation. |
| Method | [CanShowInAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInAnnotationView.md) | Gets whether this annotation can be shown in the specified [annotation view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md). |
| Method | [CanShowInMultipleAnnotationViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CanShowInMultipleAnnotationViews.md) | Gets whether this annotation can be shown in multiple [annotation views.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.md) |
| Method | [CheckSpelling](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~CheckSpelling.md) | Spell checks the text in this annotation. |
| Method | [ConvertToMultiJog](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ConvertToMultiJog.md) | Converts a note with a leader to a note with a multi-jog leader. |
| Method | [DeleteStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.md) | Deletes the specified style. |
| Method | [DeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeSelect.md) | Deselects this annotation. |
| Method | [GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md) | Gets the number of arrowheads on this symbol. |
| Method | [GetArrowHeadSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.md) | Gets the arrow head size of the specified leader on this annotation. |
| Method | [GetArrowHeadStyleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md) | Gets the arrow head style of a specific leader on this annotation. |
| Method | [GetAttachedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities.md) | Obsolete. Superseded by [IAnnotation::GetAttachedEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md). |
| Method | [GetAttachedEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md) | Obsolete. Superseded by [IAnnotation::GetAttachedEntities3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.md). |
| Method | [GetAttachedEntities3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities3.md) | Gets the entities to which this annotation is attached. |
| Method | [GetAttachedEntityCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.md) | Obsolete. Superseded by [IAnnotation::GetAtatchedEntityCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.md). |
| Method | [GetAttachedEntityCount3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount3.md) | Gets the number of entities to which this annotation is attached. |
| Method | [GetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityTypes.md) | Gets the types of entities attached to this annotation. |
| Method | [GetBentLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetBentLeader.md) | Obsolete. Superseded by [IAnnotation::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md). |
| Method | [GetDashedLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.md) | Gets whether this leader is a dashed line or a solid line. |
| Method | [GetDimXpertFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertFeature.md) | Gets the DimXpert feature associated with this annotation. |
| Method | [GetDimXpertName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDimXpertName.md) | Gets the DimXpert name for this annotation. |
| Method | [GetDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDisplayData.md) | Gets the display data for this annotation. |
| Method | [GetFlipPlaneTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetFlipPlaneTransform.md) | Gets the transformation matrix of the annotation plane in the opposite direction. |
| Method | [GetLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeader.md) | Obsolete. Superseded by [IAnnotation::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md). |
| Method | [GetLeaderAllAround](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.md) | Gets the setting for all-around symbol display of this annotation. |
| Method | [GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.md) | Gets the number of leaders on this annotation. |
| Method | [GetLeaderPerpendicular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.md) | Gets the perpendicular bent leader display setting for this annotation. |
| Method | [GetLeaderPointsAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.md) | Gets coordinate information about a specified leader on this annotation. |
| Method | [GetLeaderSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.md) | Gets the leader attachment side setting for this annotation. |
| Method | [GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md) | Gets the style of this leader. |
| Method | [GetMultiJogLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.md) | Gets the number of multi-jog leaders on this annotation. |
| Method | [GetMultiJogLeaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.md) | Gets the multi-jog leaders on this annotation. |
| Method | [GetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetName.md) | Gets the name of this annotation. |
| Method | [GetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext.md) | Obsolete. Superseded by [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md). |
| Method | [GetNext2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext2.md) | Obsolete. Superseded by [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md). |
| Method | [GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md) | Gets the next annotation. |
| Method | [GetParagraphs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetParagraphs.md) | Gets the paragraphs in this note annotation. |
| Method | [GetPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.md) | Gets the rotation matrix of the annotation relative to the X-Y plane of the model. |
| Method | [GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) | Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation. |
| Method | [GetPMIType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIType.md) | Gets the type of Product and Manufacturing Information (PMI) associated with this STEP 242 annotation. |
| Method | [GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.md) | Gets the position of this annotation. |
| Method | [GetSmartArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle.md) | Gets the setting for smart arrowhead style for this annotation. |
| Method | [GetSpecificAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.md) | Gets the specific underlying object associated with this annotation. |
| Method | [GetStyleName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.md) | Gets the name of the style applied to this annotation. |
| Method | [GetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormat.md) | Gets the text format for the specified text in this annotation. |
| Method | [GetTextFormatCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetTextFormatCount.md) | Gets the number of text formats for this annotation. |
| Method | [GetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetType.md) | Gets the type of the annotation. |
| Method | [GetUseDocTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetUseDocTextFormat.md) | Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation. |
| Method | [GetVisualProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetVisualProperties.md) | Gets the visual properties of this annotation. |
| Method | [IGetAttachedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntities.md) | Obsolete. Superseded by [IAnnotation::GetAttachedEntities2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md). |
| Method | [IGetAttachedEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityCount.md) | Obsolete. Superseded by [IAnnotation::GetAttachedEntityCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntityCount2.md). |
| Method | [IGetAttachedEntityTypes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntityTypes.md) | Gets the types of all entities attached to this annotation. |
| Method | [IGetDisplayData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetDisplayData.md) | Gets the display data for the annotation. |
| Method | [IGetLeaderPointsAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetLeaderPointsAtIndex.md) | Gets coordinate information about a specified leader on this annotation. |
| Method | [IGetMultiJogLeaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetMultiJogLeaders.md) | Gets the multi-jog leaders on this annotation. |
| Method | [IGetNext](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetNext.md) | Obsolete. Superseded by [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md). |
| Method | [IGetNext2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetNext2.md) | Obsolete. Superseded by [IAnnotation::GetNext3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetNext3.md). |
| Method | [IGetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetPosition.md) | Gets the position of this annotation. |
| Method | [IGetSpecificAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.md) | Gets the specific underlying object associated with this annotation. |
| Method | [IGetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetTextFormat.md) | Gets the text format for the specified text in this annotation. |
| Method | [IGetVisualProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetVisualProperties.md) | Gets the visual properties of this annotation. |
| Method | [IsDangling](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDangling.md) | Gets whether this annotation is dangling. |
| Method | [IsDimXpert](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IsDimXpert.md) | Gets whether the annotation is a DimXpert annotation. |
| Method | [ISetAttachedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetAttachedEntities.md) | Attaches this annotation to the specified entities. |
| Method | [ISetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ISetTextFormat.md) | Sets the text format information for the specified text within this annotation. |
| Method | [LoadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.md) | Loads the specified style. |
| Method | [SaveStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.md) | Saves the specified style. |
| Method | [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select.md) | Obsolete. Superseded by [IAnnotation::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.md). |
| Method | [Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select2.md) | Obsolete. Superseded by [IAnnotation::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.md). |
| Method | [Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.md) | Selects this annotation and marks it. |
| Method | [SelectByMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SelectByMark.md) | Obsolete. Superseded by [IAnnotation::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~Select3.md). |
| Method | [SetArrowHeadSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.md) | Sets the size of the arrow head of the specified leader on this annotation. |
| Method | [SetArrowHeadStyleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md) | Sets the arrow head style of a specific leader on this annotation. |
| Method | [SetAttachedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetAttachedEntities.md) | Attaches this annotation to the specified entities. |
| Method | [SetLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader.md) | Obsolete. Superseded by [IAnnotation::SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md). |
| Method | [SetLeader2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader2.md) | Obsolete. Superseded by [IAnnotation::SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md). |
| Method | [SetLeader3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md) | Sets the leader characteristics for this annotation. |
| Method | [SetLeaderAttachmentPointAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex.md) | Sets the specified attachment point of a leader for an annotation with the specified index. |
| Method | [SetName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetName.md) | Sets the name of this annotation. |
| Method | [SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md) | Obsolete. Superseded by [IAnnotation::SetPosition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition2.md). |
| Method | [SetPosition2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition2.md) | Sets the position of this annotation. |
| Method | [SetStyleName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.md) | Sets the style for this annotation. |
| Method | [SetTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetTextFormat.md) | Sets the text format for the specified text in this annotation. |

[Top](#top)

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::GetObjectId Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetObjectId.md)
