# Gap Property (IRipFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~Gap`

Gets or sets the gap for this rip feature.
Gets or sets the gap for this rip feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Gap As System.Double
```

```

Dim instance As IRipFeatureData
Dim value As System.Double
 
instance.Gap = value
 
value = instance.Gap
```

```

System.double Gap {get; set;}
```

```

property System.double Gap {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Gap

Remarks

|  |  |
| --- | --- |
| **If...** | **Then SOLIDWORKS returns...** |
| No value is set | 1 |
| Using the default gap | -1 |

Example

See the [IRipFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md)  
[IRipFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.md)
