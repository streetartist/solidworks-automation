# GetFaceHatches Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches`

Gets the face hatches in the view.
Gets the face hatches in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaceHatches() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetFaceHatches()
```

```

System.object GetFaceHatches()
```

```

System.Object^ GetFaceHatches(); 
```

#### Return Value

[Face hatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md) in the view

Remarks

To get the number of solid hatches in a detail, broken, or crop view, use [IView::GetSolidHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.md). To get solid hatches in detail, broken, or crop views, use [IView::GetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.md) or [IView::IGetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.md).

Example

[Get Face Hatch Data (C#)](Get_Face_Hatch_Data_Example_CSharp.htm)  
[Get Face Hatch Data (VB.NET)](Get_Face_Hatch_Data_Example_VBNET.htm)  
[Get Face Hatch Data (VBA)](Get_Face_Hatch_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetFaceHatchCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md)  
[IView::IGetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.md)  
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.md)  
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.md)
