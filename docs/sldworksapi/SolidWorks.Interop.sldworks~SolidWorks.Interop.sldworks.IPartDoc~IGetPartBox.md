# IGetPartBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetPartBox`

Gets the box enclosing the part.
Gets the box enclosing the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetPartBox( _
   ByVal NoConversion As System.Boolean _
) As System.Double
```

```

Dim instance As IPartDoc
Dim NoConversion As System.Boolean
Dim value As System.Double
 
value = instance.IGetPartBox(NoConversion)
```

```

System.double IGetPartBox( 
   System.bool NoConversion
)
```

```

System.double IGetPartBox( 
   System.bool NoConversion
) 
```

#### Parameters

*NoConversion*
:   Convert to user units or not; True retains system units, false changes to user units

#### Return Value

- in-process, unmanaged C++: Pointer to an array of 6 doubles containing the 2 diagonal points that bound the part
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The values returned are approximate and should not be used for comparison or calculation purposes. Furthermore, the bounding box may vary after rebuilding the model.

The X,Y,Z points returned are the lower- and upper-diagonal corners that bound the part with the box sides parallel to the X, Y and Z axes. The box dimensions returned enclose the part and usually close to the minimum possible size, but this is not guaranteed.

Example

[Return Box Extents (C++)](Return_Box_Extents_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
