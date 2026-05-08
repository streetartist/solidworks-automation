# SplitFaceOnParam Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~SplitFaceOnParam`

Splits and retrieves the faces on the U or V parameter
Splits and retrieves the faces on the U or V parameter

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SplitFaceOnParam( _
   ByVal Facedisp As System.Object, _
   ByVal UVFlag As System.Integer, _
   ByVal Parameter As System.Double, _
   ByRef Status As System.Boolean _
) As System.Object
```

```

Dim instance As IModeler
Dim Facedisp As System.Object
Dim UVFlag As System.Integer
Dim Parameter As System.Double
Dim Status As System.Boolean
Dim value As System.Object
 
value = instance.SplitFaceOnParam(Facedisp, UVFlag, Parameter, Status)
```

```

System.object SplitFaceOnParam( 
   System.object Facedisp,
   System.int UVFlag,
   System.double Parameter,
   out System.bool Status
)
```

```

System.Object^ SplitFaceOnParam( 
   System.Object^ Facedisp,
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
:   Position along the parametric axis at which the split is performed

*Status*
:   True if the operation was successful, false if

#### Return Value

Array of new [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ISplitFaceOnParam2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParam2.md)  
[IModeler::ISplitFaceOnParamCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ISplitFaceOnParamCount2.md)
