# GetSketch Method (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSketch`

Gets the sketch used by this view.
Gets the sketch used by this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSketch() As System.Object
```

```

Dim instance As IView
Dim value As System.Object
 
value = instance.GetSketch()
```

```

System.object GetSketch()
```

```

System.Object^ GetSketch(); 
```

#### Return Value

[Sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

Each drawing view contains an underlying sketch. The user can activate the sketch for a drawing view by double-clicking the view. Once the drawing view is active, you can add sketch directly to the view's sketch.

Example

[Get Hatching Data (VBA)](Get_Hatching_Data_Example_VB.htm)  
[Get Polylines Information (VBA)](Get_Polylines_Information_Example_VB.htm)  
[Get Sketch Point's View (VBA)](Get_Sketch_Point_s_View_Example_VB.htm)  
[Insert and Position DXF File in Drawing (VBA)](Insert_and_Position_DXF_File_in_Drawing_Example_VB.htm)  
[Get Area Hatch Data (VBA)](Get_Area_Hatch_Data_Example_VB.htm)  
[Get Area Hatch Data (VB.NET)](Get_Area_Hatch_Data_Example_VBNET.htm)  
[Get Area Hatch Data (C#)](Get_Area_Hatch_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IGetSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSketch.md)
