# SetMessage Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage`

Obsolete. Superseded by IPropertyManagerPage2::SetMessage2.
Obsolete. Superseded by [IPropertyManagerPage2::SetMessage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMessage( _
   ByVal Message As System.String, _
   ByVal Visibility As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPage2
Dim Message As System.String
Dim Visibility As System.Integer
Dim value As System.Boolean
 
value = instance.SetMessage(Message, Visibility)
```

```

System.bool SetMessage( 
   System.string Message,
   System.int Visibility
)
```

```

System.bool SetMessage( 
   System.String^ Message,
   System.int Visibility
) 
```

#### Parameters

*Message*

*Visibility*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.md)  
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.md)
