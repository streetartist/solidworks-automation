# GetMirrorPlaneType Method (IMirrorPartFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlaneType`

Gets whether the mirror plane is a face or a reference plane.
Gets whether the mirror plane is a face or a reference plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMirrorPlaneType() As System.Integer
```

```

Dim instance As IMirrorPartFeatureData
Dim value As System.Integer
 
value = instance.GetMirrorPlaneType()
```

```

System.int GetMirrorPlaneType()
```

```

System.int GetMirrorPlaneType(); 
```

#### Return Value

Type of mirror plane as defined in [swMirrorPlaneType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorPlaneType_e.html)

Remarks

Call this method to determine the type of mirror plane returned by [IMirrorPartFeatureData::GetMirrorPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlane.md).

Example

See the [IMirrorPartFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.md)  
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.md)
