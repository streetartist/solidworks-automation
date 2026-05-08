# InsertMagneticLine Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~InsertMagneticLine`

Gets and sets whether to insert magnetic lines with balloons.
Gets and sets whether to insert magnetic lines with balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InsertMagneticLine As System.Boolean
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Boolean
 
instance.InsertMagneticLine = value
 
value = instance.InsertMagneticLine
```

```

System.bool InsertMagneticLine {get; set;}
```

```

property System.bool InsertMagneticLine {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to insert magnetic lines, false to not; only valid when [IAutoBalloonOptons::Layout](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Layout.md) is not set to [swBalloonLayoutType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonLayoutType_e.html).swDetailingBalloonLayout\_Circle

Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
