# SetUserPreferenceDoubleValue Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceDoubleValue`

Obsolete. Superseded by IModelDoc2::SetUserPreferenceDoubleValue.
Obsolete. Superseded by [IModelDoc2::SetUserPreferenceDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceDoubleValue.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceDoubleValue( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetUserPreferenceDoubleValue(UserPreferenceValue, Value)
```

```

System.bool SetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
)
```

```

System.bool SetUserPreferenceDoubleValue( 
   System.int UserPreferenceValue,
   System.double Value
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
