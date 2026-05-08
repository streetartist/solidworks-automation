# Offset Property (ISMNormalCutFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~Offset`

Obsolete. See ISMNormalCutFeatureData2.
Obsolete. See [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Offset As System.Double
```

```

Dim instance As ISMNormalCutFeatureData
Dim value As System.Double
 
instance.Offset = value
 
value = instance.Offset
```

```

System.double Offset {get; set;}
```

```

property System.double Offset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= offset <= 1.0

Remarks

This property allows you to adjust the profile of the Normal Cut. Setting this property to 0.0 sets the profile to the circular edge on one side of the body. Setting it to 1.0 sets the profile to the circular edge on the opposite side of the body. A value in between 0.0 and 1.0 sets the profile to a circular edge somewhere in the middle of the body.

Example

See the [IFeatureManager::AddSMNormalCutType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddSMNormalCutType.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.md)  
[ISMNormalCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData_members.md)
