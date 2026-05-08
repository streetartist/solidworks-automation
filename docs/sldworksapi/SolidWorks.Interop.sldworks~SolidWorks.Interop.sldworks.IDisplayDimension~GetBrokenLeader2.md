# GetBrokenLeader2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetBrokenLeader2`

Gets whether this display dimension has a broken or split leader.
Gets whether this display dimension has a broken or split leader.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetBrokenLeader2() As System.Integer
```

```

Dim instance As IDisplayDimension
Dim value As System.Integer
 
value = instance.GetBrokenLeader2()
```

```

System.int GetBrokenLeader2()
```

```

System.int GetBrokenLeader2(); 
```

#### Return Value

Broken leader value as defined in [swDisplayDimensionLeaderText\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayDimensionLeaderText_e.html)

Remarks

Dimension text can be displayed above a solid leader line or the dimension leader line can be broken with the text displayed either horizontal or aligned with the leader line. You can use this method to determine which setting is used by this display dimension.

The setting can be local to the display dimension, or the display dimension might use the default document setting. This method returns a valid value only if it is using a local setting; if this display dimension uses the default document setting, it returns -1.

Use [IDisplayDimension::SetBrokenLeader2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.md) to set this value.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetUseDocBrokenLeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocBrokenLeader.md)  
[IDisplayDimension::SetBrokenLeader2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetBrokenLeader2.md)  
[IDisplayDimension::SolidLeader Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SolidLeader.md)
