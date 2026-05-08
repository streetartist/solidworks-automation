# CreateBodiesFromSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets`

Obsolete. Superseded by IModeler::CreateBodiesFromSheets2.
Obsolete. Superseded by [IModeler::CreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBodiesFromSheets( _
   ByVal Sheets As System.Object, _
   ByVal Options As System.Integer, _
   ByRef Error As System.Integer _
) As System.Object
```

```

Dim instance As IModeler
Dim Sheets As System.Object
Dim Options As System.Integer
Dim Error As System.Integer
Dim value As System.Object
 
value = instance.CreateBodiesFromSheets(Sheets, Options, Error)
```

```

System.object CreateBodiesFromSheets( 
   System.object Sheets,
   System.int Options,
   out System.int Error
)
```

```

System.Object^ CreateBodiesFromSheets( 
   System.Object^ Sheets,
   System.int Options,
   [Out] System.int Error
) 
```

#### Parameters

*Sheets*

*Options*

*Error*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
