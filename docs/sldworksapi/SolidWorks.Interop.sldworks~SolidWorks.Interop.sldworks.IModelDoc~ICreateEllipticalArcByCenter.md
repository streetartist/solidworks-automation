# ICreateEllipticalArcByCenter Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateEllipticalArcByCenter`

Obsolete. Superseded by IModelDoc2::ICreateEllipticalArcByCenter.
Obsolete. Superseded by [IModelDoc2::ICreateEllipticalArcByCenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateEllipticalArcByCenter( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) 
```

```

Dim instance As IModelDoc
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double
Dim Start As System.Double
Dim End As System.Double
 
instance.ICreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

```

void ICreateEllipticalArcByCenter( 
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor,
   ref System.double Start,
   ref System.double End
)
```

```

void ICreateEllipticalArcByCenter( 
   System.double% Center,
   System.double% Major,
   System.double% Minor,
   System.double% Start,
   System.double% End
) 
```

#### Parameters

*Center*

*Major*

*Minor*

*Start*

*End*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
