# IGetFaceHatches Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches`

Gets the face hatches in the view.
Gets the face hatches in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaceHatches( _
   ByVal NumFacesHatches As System.Integer _
) As FaceHatch
```

```

Dim instance As IView
Dim NumFacesHatches As System.Integer
Dim value As FaceHatch
 
value = instance.IGetFaceHatches(NumFacesHatches)
```

```

FaceHatch IGetFaceHatches( 
   System.int NumFacesHatches
)
```

```

FaceHatch^ IGetFaceHatches( 
   System.int NumFacesHatches
) 
```

#### Parameters

*NumFacesHatches*
:   Number of face hatches in the view

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [face hatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Remarks

Call [IView::GetFaceHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md) before calling this method to get the value for NumFacesHatches.

To get the number of solid-fill hatches in a detail, broken, or crop view, use [IView::GetSolidHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.md). To get solid hatches in detail, broken, or crop views, use [IView::GetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.md) or [IView::IGetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md)  
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.md)  
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.md)  
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.md)
