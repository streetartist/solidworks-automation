# IGetTableAnnotations Method (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~IGetTableAnnotations`

Gets the BOM table annotations for this BOM table feature.
Gets the BOM table annotations for this BOM table feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTableAnnotations( _
   ByVal Count As System.Integer _
) As BomTableAnnotation
```

```

Dim instance As IBomFeature
Dim Count As System.Integer
Dim value As BomTableAnnotation
 
value = instance.IGetTableAnnotations(Count)
```

```

BomTableAnnotation IGetTableAnnotations( 
   System.int Count
)
```

```

BomTableAnnotation^ IGetTableAnnotations( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of BOM table annotations for this BOM feature

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [IBOMTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.md) objects
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IBomFeature::GetTableAnnotationCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotationCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetTableAnnotations.md)
