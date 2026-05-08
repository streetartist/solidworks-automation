# ICreateBodiesFromSheets Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets`

Obsolete. Superseded by IModeler::ICreateBodiesFromSheets2.
Obsolete. Superseded by [IModeler::ICreateBodiesFromSheets2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateBodiesFromSheets( _
   ByVal NSheets As System.Integer, _
   ByRef Sheets As System.Object, _
   ByVal Options As System.Integer, _
   ByRef NResults As System.Integer, _
   ByRef Results As System.Object _
) As System.Integer
```

```

Dim instance As IModeler
Dim NSheets As System.Integer
Dim Sheets As System.Object
Dim Options As System.Integer
Dim NResults As System.Integer
Dim Results As System.Object
Dim value As System.Integer
 
value = instance.ICreateBodiesFromSheets(NSheets, Sheets, Options, NResults, Results)
```

```

System.int ICreateBodiesFromSheets( 
   System.int NSheets,
   ref System.object Sheets,
   System.int Options,
   out System.int NResults,
   out System.object Results
)
```

```

System.int ICreateBodiesFromSheets( 
   System.int NSheets,
   System.Object^% Sheets,
   System.int Options,
   [Out] System.int NResults,
   [Out] System.Object^ Results
) 
```

#### Parameters

*NSheets*

*Sheets*

*Options*

*NResults*

*Results*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
