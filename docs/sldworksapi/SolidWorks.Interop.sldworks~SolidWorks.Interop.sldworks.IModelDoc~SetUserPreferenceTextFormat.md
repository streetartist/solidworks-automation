# SetUserPreferenceTextFormat Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SetUserPreferenceTextFormat`

Obsolete. Superseded by IModelDoc2::SetUserPreferenceTextFormat.
Obsolete. Superseded by [IModelDoc2::SetUserPreferenceTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUserPreferenceTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer, _
   ByVal Value As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim Value As System.Object
Dim value As System.Boolean
 
value = instance.SetUserPreferenceTextFormat(UserPreferenceValue, Value)
```

```

System.bool SetUserPreferenceTextFormat( 
   System.int UserPreferenceValue,
   System.object Value
)
```

```

System.bool SetUserPreferenceTextFormat( 
   System.int UserPreferenceValue,
   System.Object^ Value
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
