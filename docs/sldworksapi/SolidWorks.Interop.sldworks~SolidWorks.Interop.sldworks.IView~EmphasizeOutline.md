# EmphasizeOutline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EmphasizeOutline`

Gets or sets whether the outlines of section views are emphasized in this drawing view.
Gets or sets whether the outlines of section views are emphasized in this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EmphasizeOutline As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.EmphasizeOutline = value
 
value = instance.EmphasizeOutline
```

```

System.bool EmphasizeOutline {get; set;}
```

```

property System.bool EmphasizeOutline {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the outlines of section views are outlined, false if not

Example

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)  
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)  
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
