# SetUserPreferenceToggle Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceToggle`

Obsolete. Superseded by IModelDoc2::SetUserPreferenceToggle.
Obsolete. Superseded by [IModelDoc2::SetUserPreferenceToggle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceToggle.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceToggle( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal OnFlag As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim OnFlag As System.Boolean
Dim value As System.Boolean
 
value = instance.SetUserPreferenceToggle(UserPreferenceValue, OnFlag)
```

```

System.bool SetUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
)
```

```

System.bool SetUserPreferenceToggle( 
   System.int UserPreferenceValue,
   System.bool OnFlag
) 
```

#### Parameters

*UserPreferenceValue*

*OnFlag*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
