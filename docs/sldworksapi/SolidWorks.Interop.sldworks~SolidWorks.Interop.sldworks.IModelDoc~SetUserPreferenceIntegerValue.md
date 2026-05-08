# SetUserPreferenceIntegerValue Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceIntegerValue`

Obsolete. Superseded by IModelDoc2::SetUserPreferenceIntegerValue.
Obsolete. Superseded by [IModelDoc2::SetUserPreferenceIntegerValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceIntegerValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceIntegerValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Integer
Dim value As System.Boolean
 
value = instance.SetUserPreferenceIntegerValue(UserPreferenceValue, Value)
```

```

System.bool SetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
)
```

```

System.bool SetUserPreferenceIntegerValue( 
   System.int UserPreferenceValue,
   System.int Value
) 
```

#### Parameters

*UserPreferenceValue*

*Value*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
