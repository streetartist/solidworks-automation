# GetUserPreferenceStringValue Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GetUserPreferenceStringValue`

Obsolete. Superseded by IModelDoc2::GetUserPreferenceStringValue.
Obsolete. Superseded by [IModelDoc2::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserPreferenceStringValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserPreferenceStringValue( _
   ByVal UserPreference As System.Integer _
) As System.String
```

```

Dim instance As IModelDoc
Dim UserPreference As System.Integer
Dim value As System.String
 
value = instance.GetUserPreferenceStringValue(UserPreference)
```

```

System.string GetUserPreferenceStringValue( 
   System.int UserPreference
)
```

```

System.String^ GetUserPreferenceStringValue( 
   System.int UserPreference
) 
```

#### Parameters

*UserPreference*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
