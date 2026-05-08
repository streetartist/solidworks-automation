# IsNameUsed Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IsNameUsed`

Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use.
Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsNameUsed( _
   ByVal Type As System.Integer, _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.IsNameUsed(Type, Name)
```

```

System.bool IsNameUsed( 
   System.int Type,
   System.string Name
)
```

```

System.bool IsNameUsed( 
   System.int Type,
   System.String^ Name
) 
```

#### Parameters

*Type*
:   Type of entity or entities whose names to check as defined by [swNameType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNameType_e.html)

*Name*
:   Name of entity

#### Return Value

True if name is in use (i.e., not valid to use again); false if the name is not in use (i.e., valid to use)

Remarks

Call this method before calling [IBody2::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Name.md) to check to see if the new name specified for the selected body is valid.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
