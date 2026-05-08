# SetName Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetName`

Sets the name of this detail circle, as displayed in the FeatureManager design tree.
Sets the name of this detail circle, as displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetName( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetName(Name)
```

```

System.bool SetName( 
   System.string Name
)
```

```

System.bool SetName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of this detail circle

#### Return Value

True if setting the detail circle name is successful, false if not

Remarks

If setting the name of a feature, then the new name must be unique in the FeatureManager design tree. If the name is not unique, then the name is not changed. Also, the name cannot contain any of the SOLIDWORKS reserved special characters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetName.md)
