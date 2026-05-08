# SolutionIndex Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~SolutionIndex`

Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature.
Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SolutionIndex As System.Integer
```

```

Dim instance As IRefPlaneFeatureData
Dim value As System.Integer
 
instance.SolutionIndex = value
 
value = instance.SolutionIndex
```

```

System.int SolutionIndex {get; set;}
```

```

property System.int SolutionIndex {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Value indicating intended plane (0-based index)

Remarks

This property corresponds to the **Other Solutions** check box that appears on the Plane PropertyManager page when there is more than one plane from which to select when creating an on-surface reference plane in SOLIDWORKS.

**IMPORTANT:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not. See the **Remarks** section in the [IRefPlaneFeatureData interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md) topic for details about reference planes and this interface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData.md)  
[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)
