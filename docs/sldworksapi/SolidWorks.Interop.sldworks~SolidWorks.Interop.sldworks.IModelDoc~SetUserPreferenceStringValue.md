# SetUserPreferenceStringValue Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceStringValue`

Obsolete. Superseded by IModelDoc2::SetUserPreferenceStringValue.
Obsolete. Superseded by [IModelDoc2::SetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceStringValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer, _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim UserPreference As System.Integer
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.SetUserPreferenceStringValue(UserPreference, Value)
```

```

System.bool SetUserPreferenceStringValue( 
   System.int UserPreference,
   System.string Value
)
```

```

System.bool SetUserPreferenceStringValue( 
   System.int UserPreference,
   System.String^ Value
) 
```

#### Parameters

*UserPreference*

*Value*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
