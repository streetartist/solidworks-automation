# IGetUserPreferenceTextFormat Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IGetUserPreferenceTextFormat`

Obsolete. Superseded by IModelDoc2::IGetUserPreferenceTextFormat.
Obsolete. Superseded by [IModelDoc2::IGetUserPreferenceTextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserPreferenceTextFormat.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetUserPreferenceTextFormat( _
   ByVal UserPreferenceValue As System.Integer _
) As TextFormat
```

```

Dim instance As IModelDoc
Dim UserPreferenceValue As System.Integer
Dim value As TextFormat
 
value = instance.IGetUserPreferenceTextFormat(UserPreferenceValue)
```

```

TextFormat IGetUserPreferenceTextFormat( 
   System.int UserPreferenceValue
)
```

```

TextFormat^ IGetUserPreferenceTextFormat( 
   System.int UserPreferenceValue
) 
```

#### Parameters

*UserPreferenceValue*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
