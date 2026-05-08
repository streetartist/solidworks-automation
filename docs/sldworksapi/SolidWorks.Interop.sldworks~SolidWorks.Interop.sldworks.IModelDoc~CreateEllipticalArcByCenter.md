# CreateEllipticalArcByCenter Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateEllipticalArcByCenter`

Obsolete. Superseded by IModelDoc2::CreateEllipticalArcByCenter.
Obsolete. Superseded by [IModelDoc2::CreateEllipticalArcByCenter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipticalArcByCenter( _
   ByVal Center As System.Object, _
   ByVal Major As System.Object, _
   ByVal Minor As System.Object, _
   ByVal Start As System.Object, _
   ByVal End As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim Center As System.Object
Dim Major As System.Object
Dim Minor As System.Object
Dim Start As System.Object
Dim End As System.Object
Dim value As System.Boolean
 
value = instance.CreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

```

System.bool CreateEllipticalArcByCenter( 
   System.object Center,
   System.object Major,
   System.object Minor,
   System.object Start,
   System.object End
)
```

```

System.bool CreateEllipticalArcByCenter( 
   System.Object^ Center,
   System.Object^ Major,
   System.Object^ Minor,
   System.Object^ Start,
   System.Object^ End
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
