# AddToolbar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar`

Obsolete. Superseded by ISldWorks::AddToolbar4.
Obsolete. Superseded by [ISldWorks::AddToolbar4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToolbar( _
   ByVal ModuleName As System.String, _
   ByVal Title As System.String, _
   ByVal SmallBitmapHandle As System.Integer, _
   ByVal LargeBitmapHandle As System.Integer _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim ModuleName As System.String
Dim Title As System.String
Dim SmallBitmapHandle As System.Integer
Dim LargeBitmapHandle As System.Integer
Dim value As System.Integer
 
value = instance.AddToolbar(ModuleName, Title, SmallBitmapHandle, LargeBitmapHandle)
```

```

System.int AddToolbar( 
   System.string ModuleName,
   System.string Title,
   System.int SmallBitmapHandle,
   System.int LargeBitmapHandle
)
```

```

System.int AddToolbar( 
   System.String^ ModuleName,
   System.String^ Title,
   System.int SmallBitmapHandle,
   System.int LargeBitmapHandle
) 
```

#### Parameters

*ModuleName*

*Title*

*SmallBitmapHandle*

*LargeBitmapHandle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
