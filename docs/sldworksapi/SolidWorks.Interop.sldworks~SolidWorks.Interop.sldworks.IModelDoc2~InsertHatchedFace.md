# InsertHatchedFace Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace`

Hatches the selected faces or closed sketch segments in a drawing.
Hatches the selected faces or closed sketch segments in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertHatchedFace() 
```

```

Dim instance As IModelDoc2
 
instance.InsertHatchedFace()
```

```

void InsertHatchedFace()
```

```

void InsertHatchedFace(); 
```

Remarks

This method supports hatching of drawings only; it does not support hatching of parts or assemblies.

Example

[Insert Hatch (VBA)](Insert_Hatch_Example_VB.htm)  
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)  
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)  
[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IView::GetFaceHatchCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md)  
[IView::GetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md)  
[IView::IGetFaceHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.md)  
[IView::ScaleHatchPattern Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ScaleHatchPattern.md)  
[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[ISketchManager::CreateRegionHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.md)  
[ISketchManager::CreateBoundaryHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.md)
