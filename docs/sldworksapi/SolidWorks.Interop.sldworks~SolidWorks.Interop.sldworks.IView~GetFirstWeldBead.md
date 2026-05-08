# GetFirstWeldBead Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldBead`

Gets the first weld bead annotation in this view.
Gets the first weld bead annotation in this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFirstWeldBead() As WeldBead
```

```

Dim instance As IView
Dim value As WeldBead
 
value = instance.GetFirstWeldBead()
```

```

WeldBead GetFirstWeldBead()
```

```

WeldBead^ GetFirstWeldBead(); 
```

#### Return Value

First [weld bead](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.md)

Example

[Get Weld Bead Symbol Data (VBA)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VB.htm)  
[Get Weld Bead Symbol Data (VB.NET)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_VBNET.htm)  
[Get Weld Bead Symbol Data (C#)](Get_Weld_Bead_End_Treatment_Symbol_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IWeldBead::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead~GetNext.md)  
[IView::IGetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldBeads.md)  
[IView::GetWeldBeads Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldBeads.md)
