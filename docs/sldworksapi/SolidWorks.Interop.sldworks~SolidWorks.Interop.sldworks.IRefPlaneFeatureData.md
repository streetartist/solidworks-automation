# IRefPlaneFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData`

Allows access to reference plane feature data.
Allows access to reference plane feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IRefPlaneFeatureData 
```

```

Dim instance As IRefPlaneFeatureData
```

```

public interface IRefPlaneFeatureData 
```

```

public interface class IRefPlaneFeatureData 
```

Remarks

Before calling any of the methods and properties on this interface, you should determine the reference plane's type because some IRefPlaneFeatureData methods and properties only work with constraint-based reference planes and some only work with non-constrained reference planes. Use [IRefPlaneFeatureData::Type2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type2.md) to determine the type of reference plane.

If IRefPlaneFeatureData::Type2 returns swRefPlaneConstraintBase, then the reference plane is constraint based. To determine if a constraint-based reference plane has angle or offset distances references, call [IRefPlaneFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type.md):

- swRefPlaneAngle is returned for angle references.
- swRefPlaneDistance is returned for offset distance references.

Otherwise, the reference plane is not constraint based. Call [IRefPlaneFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData~Type.md) to determine its type.

**NOTE:** Reference planes created in SOLIDWORKS 2010 or later are constraint based; reference planes created in SOLIDWORKS 2009 or earlier are not.

The following table shows which IRefPlaneFeatureData methods and properties to use with which types of reference planes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Method or property** | **Constraint-based** | **Constraint-based  with angle or offset distance  references** | **Not  constraint-based** |
| AccessSelections | ? | ? | ? |
| GetSelectionsCount | ? | ? | ? |
| IAccessSelections | ? | ? | ? |
| IGetSelections | ? | ? | ? |
| ISetSelections | X | ? | ? |
| ReleaseSelectionAccess | ? | ? | ? |
| Angle | X | ? | ? |
| AngleOrDistance | ? | ? | X |
| AutoSize | X | ? | ? |
| Constraint | ? | ? | X |
| Distance | X | ? | ? |
| OriginOnCurve | X | ? | ? |
| ProjectionType | X | ? | ? |
| Reference | ? | ? | X |
| ReverseDirection | X | ? | ? |
| Selections | ? (get only) | ? | ? |
| SolutionIndex | X | ? | ? |
| Type | X | ? | ? |
| Type2 | ? | ? | X |
| UseNormalPlane | X | ? | ? |

 ? = Yes  
  X = No

Example

[Insert Reference Plane (VBA)](Insert_Reference_Plane_Example_VB.htm)  
[Insert Reference Plane (VB.NET)](Insert_Reference_Plane_Example_VBNET.htm)  
[Insert Reference Plane (C#)](Insert_Reference_Plane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)
