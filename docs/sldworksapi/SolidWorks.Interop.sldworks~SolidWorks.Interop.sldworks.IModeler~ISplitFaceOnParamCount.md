# ISplitFaceOnParamCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount`

Obsolete. Superseded by IModeler::ISplitFaceOnParamCount2.
Obsolete. Superseded by [IModeler::ISplitFaceOnParamCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISplitFaceOnParamCount( _
   ByVal Facedisp As Face, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Integer
```

```

Dim instance As IModeler
Dim Facedisp As Face
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Integer
 
value = instance.ISplitFaceOnParamCount(Facedisp, UVFlag, Parameter, Status)
```

```

System.int ISplitFaceOnParamCount( 
   Face Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

```

System.int ISplitFaceOnParamCount( 
   Face^ Facedisp,
   System.int UVFlag,
   System.double Parameter,
   [Out] System.bool Status
) 
```

#### Parameters

*Facedisp*

*UVFlag*

*Parameter*

*Status*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)
