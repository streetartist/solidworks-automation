# ISplitFaceOnParamCount2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2`

Sets up and counts the number of new faces split on the U or V parameter.
Sets up and counts the number of new faces split on the U or V parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISplitFaceOnParamCount2( _
   ByVal Facedisp As Face2, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Integer
```

```

Dim instance As IModeler
Dim Facedisp As Face2
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Integer
 
value = instance.ISplitFaceOnParamCount2(Facedisp, UVFlag, Parameter, Status)
```

```

System.int ISplitFaceOnParamCount2( 
   Face2 Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

```

System.int ISplitFaceOnParamCount2( 
   Face2^ Facedisp,
   System.int UVFlag,
   System.double Parameter,
   [Out] System.bool Status
) 
```

#### Parameters

*Facedisp*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to split

*UVFlag*
:   Parametric axis; either swSplitFaceOnParamU or swSplitFaceOnParamV

*Parameter*
:   Position along the parametric axis at which the split will be performed

*Status*
:   True if the operation was successful, false if not

#### Return Value

Number of new faces

Remarks

The split is defined by calling this method. Then, you can retrieve the list of new faces by using [IModeler::ISplitFaceOnParam2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::SplitFaceOnParam Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam.md)
