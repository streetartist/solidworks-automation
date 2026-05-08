# DefineJointPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint`

Gets or sets whether to define a joint point.
Gets or sets whether to define a joint point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefineJointPoint As System.Boolean
```

```

Dim instance As IUniversalJointMateFeatureData
Dim value As System.Boolean
 
instance.DefineJointPoint = value
 
value = instance.DefineJointPoint
```

```

System.bool DefineJointPoint {get; set;}
```

```

property System.bool DefineJointPoint {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to define a joint point, false to not

Remarks

If this property is set to true, then specify [IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.md).

Example

See the [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUniversalJointMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.md)  
[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.md)
