# PositionLocked Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~PositionLocked`

Gets or sets whether this drawing view's position is locked.
Gets or sets whether this drawing view's position is locked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PositionLocked As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.PositionLocked = value
 
value = instance.PositionLocked
```

```

System.bool PositionLocked {get; set;}
```

```

property System.bool PositionLocked {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if view position is locked, false if not

Example

[Get View Bounding Box and Position (VBA)](Get_View_Bounding_Box_and_Position_Example_VB.htm)  
[Get View Bounding Box and Position (VB.NET)](Get_View_Bounding_Box_and_Position_Example_VBNET.htm)  
[Get View Bounding Box and Position (C#)](Get_View_Bounding_Box_and_Position_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::Position Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.md)
