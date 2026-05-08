# IGetProfileItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~IGetProfileItems`

Gets the sketch segments that make up this detail circle profile.
Gets the sketch segments that make up this detail circle profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetProfileItems( _
   ByVal Count As System.Integer _
) As SketchSegment
```

```

Dim instance As IDetailCircle
Dim Count As System.Integer
Dim value As SketchSegment
 
value = instance.IGetProfileItems(Count)
```

```

SketchSegment IGetProfileItems( 
   System.int Count
)
```

```

SketchSegment^ IGetProfileItems( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of sketch segments that make up this detail circle profile

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) that make up this detail circle profile

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IDetailCircle::GetProfileItemsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItemsCount.md) before calling this method to determine the size of the array.

Do not modify the sketch segments returned by this method. This method only provides information about the profile geometry of the detail circle. To modify a detail circle, use [IDetailCircle::SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetParameters.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetProfileItems Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetProfileItems.md)
