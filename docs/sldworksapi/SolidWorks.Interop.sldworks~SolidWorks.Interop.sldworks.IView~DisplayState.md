# DisplayState Property (IView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~DisplayState`

Gets or sets the name of the display state for this drawing view.
Gets or sets the name of the display state for this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayState As System.String
```

```

Dim instance As IView
Dim value As System.String
 
instance.DisplayState = value
 
value = instance.DisplayState
```

```

System.string DisplayState {get; set;}
```

```

property System.String^ DisplayState {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of the display state

Example

[Get Display State for Each Drawing View (C#)](Get_Display_State_for_Each_Drawing_View_Example_CSharp.htm)  
[Get Display State for Each Drawing View (VB.NET)](Get_Display_State_for_Each_Drawing_View_Example_VBNET.htm)  
[Get Display State for Each Drawing View (VBA)](Get_Display_State_for_Each_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
