# LowerText Property (IStackedBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~LowerText`

Gets and sets the lower text of the balloons.
Gets and sets the lower text of the balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LowerText As System.String
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.String
 
instance.LowerText = value
 
value = instance.LowerText
```

```

System.string LowerText {get; set;}
```

```

property System.String^ LowerText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Lower text of the balloons (see **Remarks**)

Remarks

This property is valid only when [IStackedBalloonOptions::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~Style.md) is set to [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS\_SplitCirc. See the SOLIDWORKS Help for additional details about stacked balloons.

Example

See [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.md)
