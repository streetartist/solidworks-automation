# JointPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint`

Gets or sets the joint point of this universal joint mate.
Gets or sets the joint point of this universal joint mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property JointPoint As System.Object
```

```

Dim instance As IUniversalJointMateFeatureData
Dim value As System.Object
 
instance.JointPoint = value
 
value = instance.JointPoint
```

```

System.object JointPoint {get; set;}
```

```

property System.Object^ JointPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) or [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md)

Remarks

This property is valid only if [IUniversalJointMateFeatureData::DefineJointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUniversalJointMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.md)  
[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.md)
