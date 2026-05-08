# IGetTessTriStrips Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTessTriStrips`

Gets the vertices that make up the shaded picture tessellation for this component.
Gets the vertices that make up the shaded picture tessellation for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTessTriStrips( _
   ByVal NoConversion As System.Boolean _
) As System.Single
```

```

Dim instance As IComponent2
Dim NoConversion As System.Boolean
Dim value As System.Single
 
value = instance.IGetTessTriStrips(NoConversion)
```

```

System.float IGetTessTriStrips( 
   System.bool NoConversion
)
```

```

System.float IGetTessTriStrips( 
   System.bool NoConversion
) 
```

#### Parameters

*NoConversion*
:   True prohibits conversion to user units from system units, false does not

#### Return Value

- in-process, unmanaged C++: Pointer to an array of floats (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Tessellation information is available only when the component is loaded as lightweight.

These triangles are intended for graphical display purposes and do not represent a tessellation that could be used, for example, by a machining application. If you need the type of accuracy associated with a machining product, you should traverse the body faces and extract the topology and geometry data to create your own faceting.

where:

- *FaceCount*= number of faces on the body
- *StripCount*  = total number of strips on the body
- *VertexCount* x 3 = total number of vertices. Multiplied by three to cover X,Y, and Z
- *NumStrips* = number of strips on a particular face
- *VertexPerStrip* = an array containing the number of vertex points on particular face strip
- *VertexPoints* = an array of X,Y,Z points for each vertex on the particular face strip

Because the returned array elements are of type float, and *FaceCount*, *StripCount*, *VertexCount*, *NumStrips*, and the elements of *VertexPerStrip* are integers that have been packed into the return array elements, and you must [unpack](sldworksAPIProgGuide.chm::/OVERVIEW/Unpacking_Double_Arrays_into_Integer_Pairs_in_Visual_Basic_.NET_and_Visual_Basic.htm) them before you can use them.

For example:

- sa[0] = number of faces
- sa[1] = total number of strips
- sa[2] = total number of vertices x 3 (i.e., - data values)

For each face:

- sa[3] = number of strips in this face
- sa[4] = number of vertices in first strip of this face
- sa[5] = number of vertices in second strip of this face

> ...

- sa[3 + sa[3&cd; = number of vertices in last strip of this face

For each strip, i:

- sa[3 + sa[3] + 1] = X value of first vertex in this strip of the face
- sa[3 + sa[3] + 2] = Y value of first vertex in this strip of the face
- sa[3 + sa[3] + 3] = Z value of first vertex in this strip of the face
- sa[3 + sa[3] + 4] = X value of second vertex in this strip of the face

> ...

- sa[3 + sa[3] + (sa[3+i] x 3)] = Z value of last vertex in this strip of the face

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetTessTriStrips Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTessTriStrips.md)
