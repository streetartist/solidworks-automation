# ICreateSheetBodyByFaceExtension Method (IFace)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~ICreateSheetBodyByFaceExtension`

Obsolete. Superseded by IFace2::ICreateSheetBodyByFaceExtension.
Obsolete. Superseded by [IFace2::ICreateSheetBodyByFaceExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSheetBodyByFaceExtension( _
   ByRef BoxLowIn As System.Double, _
   ByRef BoxHighIn As System.Double _
) As Body
```

```

Dim instance As IFace
Dim BoxLowIn As System.Double
Dim BoxHighIn As System.Double
Dim value As Body
 
value = instance.ICreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

```

Body ICreateSheetBodyByFaceExtension( 
   ref System.double BoxLowIn,
   ref System.double BoxHighIn
)
```

```

Body^ ICreateSheetBodyByFaceExtension( 
   System.double% BoxLowIn,
   System.double% BoxHighIn
) 
```

#### Parameters

*BoxLowIn*

*BoxHighIn*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.md)  
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.md)
