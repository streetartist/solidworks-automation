# UpperText Property (IAutoBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~UpperText`

Gets and sets the upper text of the balloons.
Gets and sets the upper text of the balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpperText As System.String
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.String
 
instance.UpperText = value
 
value = instance.UpperText
```

```

System.string UpperText {get; set;}
```

```

property System.String^ UpperText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Upper text of the balloons

Remarks

You can only get or set the upper text in a BOM autoballoon using [INote::GetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBomBalloonText.md) or [INote::SetBomBalloonText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~SetBomBalloonText.md) after [inserting a BOM balloon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md).

See the SOLIDWORKS Help for additional details about autoballoons.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
