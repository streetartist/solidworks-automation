# Initialize Method (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize`

Initializes this simple fillet feature to the specified type.
Initializes this simple fillet feature to the specified type.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Initialize( _
   ByVal FilletType As System.Integer _
) As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim FilletType As System.Integer
Dim value As System.Boolean
 
value = instance.Initialize(FilletType)
```

```

System.bool Initialize( 
   System.int FilletType
)
```

```

System.bool Initialize( 
   System.int FilletType
) 
```

#### Parameters

*FilletType*
:   Simple fillet type as defined in [swSimpleFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletType_e.html)

#### Return Value

True if the simple fillet feature is initialized, false if not

Remarks

After you initialize this data object with a fillet type, you need to narrow the fillet type by specifying [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.md).

Example

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md) and [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md) introductory examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
