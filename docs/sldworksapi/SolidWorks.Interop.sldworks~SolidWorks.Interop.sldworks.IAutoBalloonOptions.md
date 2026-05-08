# IAutoBalloonOptions Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions`

Allows access to auto balloon options.
Allows access to auto balloon options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IAutoBalloonOptions 
```

```

Dim instance As IAutoBalloonOptions
```

```

public interface IAutoBalloonOptions 
```

```

public interface class IAutoBalloonOptions 
```

Remarks

To automatically create BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call [IDrawingDoc::CreateAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.md) to create IAutoBalloonOptions object.
3. Set the properties on IAutoBalloonOptions.
4. Pass IAutoBalloonOptions in a call to [IDrawingDoc::AutoBalloon5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.md).

Example

[Add Auto Balloons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)  
[Add Auto Balloons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)  
[Add Auto Balloons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)
