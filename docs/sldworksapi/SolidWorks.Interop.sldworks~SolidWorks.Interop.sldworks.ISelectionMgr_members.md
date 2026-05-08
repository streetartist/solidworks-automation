# ISelectionMgr Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members`

Allows you to get information about selected objects, obtain API objects representing the selected item, and get your selection coordinates interpreted in model or sketch space.
The following tables list the members exposed by [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [EnableContourSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableContourSelection.md) | Enables and disables contour selection. |
| Property | [EnableSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~EnableSelection.md) | Enables or disables selection. |
| Property | [SelectionColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SelectionColor.md) | Gets or sets the selection color. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) | Adds the specified object to the selection list. |
| Method | [AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md) | Adds the specified objects to the selection list. |
| Method | [ClearSelectionColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ClearSelectionColors.md) | Clears all of selection color settings. |
| Method | [CreateCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout.md) | Obsolete. Superseded by [ISelectionMgr::CreateCallout2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.md). |
| Method | [CreateCallout2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateCallout2.md) | Creates a callout for the selection. |
| Method | [CreateSelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateSelectData.md) | Creates a [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object to use as argument with Select methods. |
| Method | [DeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect.md) | Obsolete. Superseded by [ISelectionMgr::DeSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md). |
| Method | [DeSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~DeSelect2.md) | Deselects the specified entity. |
| Method | [GetPreSelectedObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetPreSelectedObject.md) | Gets the preselected object when the preselection notify event is fired. |
| Method | [GetSelectByIdSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectByIdSpecification.md) | Gets the selection specification for the specified object. |
| Method | [GetSelectedCoordSysElement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedCoordSysElement.md) | Gets the selected coordinate system element. |
| Method | [GetSelectedObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [GetSelectedObject2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject2.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [GetSelectedObject3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject3.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [GetSelectedObject4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject4.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [GetSelectedObject5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject5.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) | Gets the selected object. |
| Method | [GetSelectedObjectCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md). |
| Method | [GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md) | Gets the number of selected objects. |
| Method | [GetSelectedObjectLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md). |
| Method | [GetSelectedObjectLoop2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.md) | Gets the loop, if selected, for the selected edge. |
| Method | [GetSelectedObjectMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectMark.md) | Gets the value of the mark for the specified selection. |
| Method | [GetSelectedObjectsComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md). |
| Method | [GetSelectedObjectsComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent2.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md). |
| Method | [GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.md). |
| Method | [GetSelectedObjectsComponent4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent4.md) | Gets the selected component in an assembly or drawing. |
| Method | [GetSelectedObjectsDrawingView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsDrawingView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md). |
| Method | [GetSelectedObjectsDrawingView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsDrawingView2.md) | Gets the drawing view for the selected object. |
| Method | [GetSelectedObjectsFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsFace.md) | Gets the face of the specified selection if the specified selection is a [silhouette edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.md). |
| Method | [GetSelectedObjectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md). |
| Method | [GetSelectedObjectType2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType2.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md). |
| Method | [GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md) | Gets the type of object selected. |
| Method | [GetSelectionPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md). |
| Method | [GetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPoint2.md) | Gets the selected point in model space coordinates from the currently selected object. |
| Method | [GetSelectionPointInSketchSpace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectionPointInSketchSpace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md). |
| Method | [GetSelectionPointInSketchSpace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionPointInSketchSpace2.md) | Gets the selection point projected on to the active sketch and returned in sketch space. |
| Method | [GetSelectionSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectionSpecification.md) | Gets the selection specification at the specified index of the current selection list. |
| Method | [IDeSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect.md) | Obsolete. Superseded by [ISelectionMgr::IDeSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md). |
| Method | [IDeSelect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IDeSelect2.md) | Deselects the specified entity. |
| Method | [IGetSelectedObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObject.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [IGetSelectedObject2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObject2.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [IGetSelectedObject3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObject3.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [IGetSelectedObject4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObject4.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). |
| Method | [IGetSelectedObjectsComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObjectsComponent.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md). |
| Method | [IGetSelectedObjectsComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectedObjectsComponent2.md) | Obsolete. Superseded by [ISelectionMgr::GetSelectedObjectsComponent3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectsComponent3.md). |
| Method | [IGetSelectionPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint.md) | Obsolete. Superseded by [ISelectionMgr::IGetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md). |
| Method | [IGetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPoint2.md) | Gets the selected point in model space coordinates from the currently selected object. |
| Method | [IGetSelectionPointInSketchSpace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace.md) | Obsolete. Superseded by [ISelectionMgr::IGetSelectionPointInSketchSpace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md). |
| Method | [IGetSelectionPointInSketchSpace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IGetSelectionPointInSketchSpace2.md) | Gets the selection point projected on to the active sketch and returned in sketch space. |
| Method | [IsCoordSysElementSelected](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsCoordSysElementSelected.md) | Gets whether the selection is a coordinate system element. |
| Method | [IsInEditTarget](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget.md) | Obsolete. Superseded by [ISelectionMgr::IsInEditTarget2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.md). |
| Method | [IsInEditTarget2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.md) | Gets whether the selected object is in the edit target. |
| Method | [ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.md) | Obsolete. Superseded by [ISelectionMgr::ResumeSelectionList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2.md). |
| Method | [ResumeSelectionList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2.md) | Reinstates the previously suspended selection list. |
| Method | [SetCallout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetCallout.md) | Adds a callout to the currently selected object. |
| Method | [SetSelectedObjectMark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectedObjectMark.md) | Sets the mark value for the specified selection. |
| Method | [SetSelectionPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint.md) | Obsolete. Superseded by [ISelectionMgr::SetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.md). |
| Method | [SetSelectionPoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SetSelectionPoint2.md) | Sets the selection point in model space. |
| Method | [SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) | Suspends the current selection list. |

[Top](#top)

 

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)
