# BalloonsPerLine Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~BalloonsPerLine`

Gets and sets the number of stacked balloons per line.
Gets and sets the number of stacked balloons per line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BalloonsPerLine As System.Integer
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.Integer
 
instance.BalloonsPerLine = value
 
value = instance.BalloonsPerLine
```

```

System.int BalloonsPerLine {get; set;}
```

```

property System.int BalloonsPerLine {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of balloons per line; specify a number >= 2

Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

Example

See [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.md)
