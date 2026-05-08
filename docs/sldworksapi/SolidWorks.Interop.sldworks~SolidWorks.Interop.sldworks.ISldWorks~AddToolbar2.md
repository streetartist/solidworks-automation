# AddToolbar2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar2`

Obsolete. Superseded by ISldWorks::AddToolbar4.
Obsolete. Superseded by [ISldWorks::AddToolbar4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbar2( _
   ByVal ModuleNameIn As System.String, _
   ByVal TitleIn As System.String, _
   ByVal SmallBitmapHandleIn As System.Integer, _
   ByVal LargeBitmapHandleIn As System.Integer, _
   ByVal MenuPosIn As System.Integer, _
   ByVal DecTemplateTypeIn As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim ModuleNameIn As System.String
Dim TitleIn As System.String
Dim SmallBitmapHandleIn As System.Integer
Dim LargeBitmapHandleIn As System.Integer
Dim MenuPosIn As System.Integer
Dim DecTemplateTypeIn As System.Integer
Dim value As System.Integer
 
value = instance.AddToolbar2(ModuleNameIn, TitleIn, SmallBitmapHandleIn, LargeBitmapHandleIn, MenuPosIn, DecTemplateTypeIn)
```

```

System.int AddToolbar2( 
   System.string ModuleNameIn,
   System.string TitleIn,
   System.int SmallBitmapHandleIn,
   System.int LargeBitmapHandleIn,
   System.int MenuPosIn,
   System.int DecTemplateTypeIn
)
```

```

System.int AddToolbar2( 
   System.String^ ModuleNameIn,
   System.String^ TitleIn,
   System.int SmallBitmapHandleIn,
   System.int LargeBitmapHandleIn,
   System.int MenuPosIn,
   System.int DecTemplateTypeIn
) 
```

#### Parameters

*ModuleNameIn*

*TitleIn*

*SmallBitmapHandleIn*

*LargeBitmapHandleIn*

*MenuPosIn*

*DecTemplateTypeIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
