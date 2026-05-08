# View Property (ISelectData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~View`

Gets or sets the drawing view that contains the selected object.
Gets or sets the drawing view that contains the selected object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property View As View
```

```

Dim instance As ISelectData
Dim value As View
 
instance.View = value
 
value = instance.View
```

```

View View {get; set;}
```

```

property View^ View {
   View^ get();
   void set (    View^ value);
}
```

#### Property Value

[View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) that contains the selected object

Example

[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)  
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)  
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.md)
