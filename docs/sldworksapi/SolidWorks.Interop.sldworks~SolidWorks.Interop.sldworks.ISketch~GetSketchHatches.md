# GetSketchHatches Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSketchHatches`

Gets an array of sketch hatches that exist in this sketch.
Gets an array of sketch hatches that exist in this sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketchHatches() As System.Object
```

```

Dim instance As ISketch
Dim value As System.Object
 
value = instance.GetSketchHatches()
```

```

System.object GetSketchHatches()
```

```

System.Object^ GetSketchHatches(); 
```

#### Return Value

Array of [sketch hatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)

Remarks

For information about hatches:

- in drawing views, use [IView::GetFaceHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatchCount.md), [IView::GetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFaceHatches.md), and [IView::IGetFaceHatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFaceHatches.md).
- detail, broken, or crop views, use [IView::GetSolidHatchCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchCount.md), [IView::GetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSolidHatchInfo.md), and [IView::IGetSolidHatchInfo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSolidHatchInfo.md)

Example

[Get Area Hatch (VBA)](Get_Area_Hatch_Data_Example_VB.htm)  
[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)  
[Insert Hatch (VBA)](Insert_Hatch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)  
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.md)  
[ISketch::IEnumSketchHatches Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IEnumSketchHatches.md)
