# Type Property (ISimulationDamperFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData~Type`

Gets the type of damper. NOTE: This property is a get-only property. Set is not implemented.
Gets the type of damper.  
  
**NOTE: This property is a get-only property. Set is not implemented.**

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type As System.Integer
```

```

Dim instance As ISimulationDamperFeatureData
Dim value As System.Integer
 
value = instance.Type
```

```

System.int Type {get;}
```

```

property System.int Type {
   System.int get();
}
```

#### Property Value

Type of damper as defined in [swSimulationDamperType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimulationDamperType_e.html)

Example

See [ISimulationDamperFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationDamperFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData.md)  
[ISimulationDamperFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.md)
